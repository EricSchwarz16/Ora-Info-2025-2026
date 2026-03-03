import random
import threading
import time


TOTAL_CARS = 20
MAX_CARS = 3
MAX_WASH_SECONDS = 10
PRICE_PER_CAR = 25
MAX_ARRIVAL_DELAY = 2.0


class CarWashMonitor:
    def __init__(self):
        self.max_cars = MAX_CARS
        self.total_cars = TOTAL_CARS
        self.max_wash_seconds = MAX_WASH_SECONDS
        self.price_per_car = PRICE_PER_CAR
        self.max_arrival_delay = MAX_ARRIVAL_DELAY

        self.slots = threading.Semaphore(self.max_cars)
        self.panic_event = threading.Event()
        self.state_lock = threading.Lock()
        self.print_lock = threading.Lock()

        self.earnings = 0
        self.cars_inside = 0
        self.cars_finished_paid = 0
        self.cars_canceled_outside = 0
        self.cars_evacuated_inside = 0

    def log(self, message: str) -> None:
        with self.print_lock:
            print(message)

    def panic_listener(self) -> None:
        self.log("Tasteaza panica si apasa Enter pentru evacuare de urgenta.")
        try:
            while not self.panic_event.is_set():
                command = input().strip().lower()
                if command in {"panica"}:
                    self.panic_event.set()
                    self.log("\n!!! PANICA ACTIVATA: masinile din exterior sunt anulate, iar cele din interior ies fara plata !!!")
                    break
                if command:
                    self.log("Comanda necunoscuta. Foloseste: panica")
        except EOFError:
            return

    def update_outside_cancel(self, car_id: int) -> None:
        with self.state_lock:
            self.cars_canceled_outside += 1
        self.log(f"Masina #{car_id} a fost anulata la bariera.")

    def update_inside_enter(self, car_id: int) -> None:
        with self.state_lock:
            self.cars_inside += 1
            inside_now = self.cars_inside
        self.log(f"Masina #{car_id} a intrat in spalatorie. In interior: {inside_now}|{self.max_cars}")

    def update_inside_exit(self, car_id: int, paid: bool) -> None:
        with self.state_lock:
            self.cars_inside -= 1
            if paid:
                self.cars_finished_paid += 1
                self.earnings += self.price_per_car
                inside_now = self.cars_inside
                total = self.earnings
            else:
                self.cars_evacuated_inside += 1
                inside_now = self.cars_inside
                total = self.earnings

        if paid:
            self.log(f"Masina #{car_id} a iesit dupa spalare. A platit {self.price_per_car} lei. Total incasari: {total} lei")
        else:
            self.log(f"Masina #{car_id} a fost evacuata de urgenta. Fara plata. In interior: {inside_now}/{self.max_cars}")

    def car_flow(self, car_id: int) -> None:
        arrival_delay = random.uniform(0, self.max_arrival_delay)
        time.sleep(arrival_delay)

        if self.panic_event.is_set():
            self.update_outside_cancel(car_id)
            return

        self.log(f"Masina #{car_id} a ajuns la bariera si asteapta loc.")

        entered = False
        while not self.panic_event.is_set():
            entered = self.slots.acquire(timeout=0.2)
            if entered:
                break

        if not entered:
            self.update_outside_cancel(car_id)
            return

        self.update_inside_enter(car_id)

        wash_time = random.randint(1, self.max_wash_seconds)
        elapsed = 0
        while elapsed < wash_time and not self.panic_event.is_set():
            time.sleep(1)
            elapsed += 1

        paid = elapsed >= wash_time and not self.panic_event.is_set()
        self.update_inside_exit(car_id, paid)
        self.slots.release()

    def run(self) -> None:
        listener = threading.Thread(target=self.panic_listener, daemon=True)
        listener.start()

        self.log(
            f"Simulare pornita: {self.total_cars} masini, max {self.max_cars} in spalatorie, pret {self.price_per_car} lei/masina."
        )

        car_threads = []
        for car_id in range(1, self.total_cars + 1):
            thread = threading.Thread(target=self.car_flow, args=(car_id,))
            car_threads.append(thread)
            thread.start()

        for thread in car_threads:
            thread.join()

        self.print_summary()

    def print_summary(self) -> None:
        with self.state_lock:
            paid = self.cars_finished_paid
            canceled = self.cars_canceled_outside
            evacuated = self.cars_evacuated_inside
            total = self.earnings

        self.log("\n===== RAPORT FINAL =====")
        self.log(f"Masini spalate si platite: {paid}")
        self.log(f"Masini anulate la bariera: {canceled}")
        self.log(f"Masini evacuate din interior: {evacuated}")
        self.log(f"Incasari totale: {total} lei")


def main() -> None:
    if TOTAL_CARS <= 0 or MAX_CARS <= 0 or MAX_WASH_SECONDS <= 0 or PRICE_PER_CAR < 0 or MAX_ARRIVAL_DELAY < 0:
        raise ValueError("Toate valorile trebuie sa fie valide: > 0 pentru masini/capacitate/timp, >= 0 pentru pret si delay.")

    monitor = CarWashMonitor()
    monitor.run()


if __name__ == "__main__":
    main()
