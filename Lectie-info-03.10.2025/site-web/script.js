// DOM Elements
const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");
const loginBtn = document.querySelector(".btn-login");
const registerBtn = document.querySelector(".btn-register");
const loginModal = document.getElementById("loginModal");
const registerModal = document.getElementById("registerModal");
const closeBtns = document.querySelectorAll(".close");
const showRegisterBtn = document.getElementById("showRegister");
const showLoginBtn = document.getElementById("showLogin");
const mentorsGrid = document.getElementById("mentorsGrid");
const filterBtns = document.querySelectorAll(".filter-btn");
const contactForm = document.getElementById("contactForm");

// Sample mentor data
const mentorsData = [
  {
    id: 1,
    name: "Prof. Ana Popescu",
    specialty: "Matematică",
    category: "math",
    rating: 4.9,
    reviews: 127,
    price: "80 lei/oră",
    avatar: "fas fa-user-graduate",
    description: "Profesor de matematică cu 15 ani experiență",
  },
  {
    id: 2,
    name: "Dr. Mihai Ionescu",
    specialty: "Fizică & Chimie",
    category: "science",
    rating: 4.8,
    reviews: 89,
    price: "90 lei/oră",
    avatar: "fas fa-atom",
    description: "Doctor în fizică, specialist în științe exacte",
  },
  {
    id: 3,
    name: "Ing. Cristina Moldovan",
    specialty: "Programare",
    category: "programming",
    rating: 5.0,
    reviews: 156,
    price: "100 lei/oră",
    avatar: "fas fa-code",
    description: "Software engineer cu experiență în educație",
  },
  {
    id: 4,
    name: "Prof. Elena Radu",
    specialty: "Engleză",
    category: "languages",
    rating: 4.7,
    reviews: 203,
    price: "70 lei/oră",
    avatar: "fas fa-language",
    description: "Profesor de limbi străine certificat Cambridge",
  },
  {
    id: 5,
    name: "Dr. Alexandru Stan",
    specialty: "Biologie",
    category: "science",
    rating: 4.9,
    reviews: 78,
    price: "85 lei/oră",
    avatar: "fas fa-microscope",
    description: "Cercetător în biologie, pasionat de educație",
  },
  {
    id: 6,
    name: "Ing. Maria Georgescu",
    specialty: "Python & AI",
    category: "programming",
    rating: 4.8,
    reviews: 134,
    price: "120 lei/oră",
    avatar: "fas fa-robot",
    description: "Specialist AI cu background educațional",
  },
  {
    id: 7,
    name: "Prof. Andrei Vlad",
    specialty: "Geometrie",
    category: "math",
    rating: 4.6,
    reviews: 92,
    price: "75 lei/oră",
    avatar: "fas fa-shapes",
    description: "Expert în geometrie și trigonometrie",
  },
  {
    id: 8,
    name: "Dna. Carmen Dumitrescu",
    specialty: "Franceză",
    category: "languages",
    rating: 4.9,
    reviews: 167,
    price: "75 lei/oră",
    avatar: "fas fa-flag",
    description: "Native speaker, 20 ani experiență predare",
  },
];

// Initialize app
document.addEventListener("DOMContentLoaded", function () {
  initializeApp();
});

function initializeApp() {
  setupEventListeners();
  renderMentors("all");
  animateOnScroll();
  setupSmoothScrolling();
}

// Event Listeners
function setupEventListeners() {
  // Mobile menu toggle
  if (hamburger) {
    hamburger.addEventListener("click", toggleMobileMenu);
  }

  // Modal controls
  if (loginBtn) {
    loginBtn.addEventListener("click", () => openModal(loginModal));
  }

  if (registerBtn) {
    registerBtn.addEventListener("click", () => openModal(registerModal));
  }

  if (showRegisterBtn) {
    showRegisterBtn.addEventListener("click", (e) => {
      e.preventDefault();
      closeModal(loginModal);
      openModal(registerModal);
    });
  }

  if (showLoginBtn) {
    showLoginBtn.addEventListener("click", (e) => {
      e.preventDefault();
      closeModal(registerModal);
      openModal(loginModal);
    });
  }

  // Close modals
  closeBtns.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      const modal = e.target.closest(".modal");
      closeModal(modal);
    });
  });

  // Close modal when clicking outside
  window.addEventListener("click", (e) => {
    if (e.target.classList.contains("modal")) {
      closeModal(e.target);
    }
  });

  // Filter buttons
  filterBtns.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      const category = e.target.dataset.category;
      filterMentors(category);

      // Update active button
      filterBtns.forEach((b) => b.classList.remove("active"));
      e.target.classList.add("active");
    });
  });

  // Contact form
  if (contactForm) {
    contactForm.addEventListener("submit", handleContactForm);
  }

  // Navbar scroll effect
  window.addEventListener("scroll", handleNavbarScroll);

  // Close mobile menu when clicking on links
  document.querySelectorAll(".nav-link").forEach((link) => {
    link.addEventListener("click", () => {
      if (navMenu.classList.contains("active")) {
        toggleMobileMenu();
      }
    });
  });
}

// Mobile menu toggle
function toggleMobileMenu() {
  navMenu.classList.toggle("active");
  hamburger.classList.toggle("active");

  // Animate hamburger
  const spans = hamburger.querySelectorAll("span");
  spans.forEach((span, index) => {
    if (hamburger.classList.contains("active")) {
      if (index === 0)
        span.style.transform = "rotate(45deg) translate(5px, 5px)";
      if (index === 1) span.style.opacity = "0";
      if (index === 2)
        span.style.transform = "rotate(-45deg) translate(7px, -6px)";
    } else {
      span.style.transform = "none";
      span.style.opacity = "1";
    }
  });
}

// Modal functions
function openModal(modal) {
  if (modal) {
    modal.style.display = "block";
    document.body.style.overflow = "hidden";
    modal.querySelector(".modal-content").classList.add("fade-in");
  }
}

function closeModal(modal) {
  if (modal) {
    modal.style.display = "none";
    document.body.style.overflow = "auto";
  }
}

// Render mentors
function renderMentors(category) {
  if (!mentorsGrid) return;

  const filteredMentors =
    category === "all"
      ? mentorsData
      : mentorsData.filter((mentor) => mentor.category === category);

  mentorsGrid.innerHTML = filteredMentors
    .map(
      (mentor) => `
        <div class="mentor-card fade-in" data-category="${mentor.category}">
            <div class="mentor-avatar">
                <i class="${mentor.avatar}"></i>
            </div>
            <div class="mentor-info">
                <h3 class="mentor-name">${mentor.name}</h3>
                <p class="mentor-specialty">${mentor.specialty}</p>
                <div class="mentor-rating">
                    <div class="stars">${generateStars(mentor.rating)}</div>
                    <span>${mentor.rating} (${mentor.reviews} recenzii)</span>
                </div>
                <p class="mentor-description">${mentor.description}</p>
                <div class="mentor-price">${mentor.price}</div>
                <button class="mentor-btn" onclick="contactMentor(${
                  mentor.id
                })">Contactează</button>
            </div>
        </div>
    `
    )
    .join("");
}

// Filter mentors
function filterMentors(category) {
  renderMentors(category);
}

// Generate star rating
function generateStars(rating) {
  const fullStars = Math.floor(rating);
  const hasHalfStar = rating % 1 !== 0;
  let stars = "";

  for (let i = 0; i < fullStars; i++) {
    stars += '<i class="fas fa-star"></i>';
  }

  if (hasHalfStar) {
    stars += '<i class="fas fa-star-half-alt"></i>';
  }

  const emptyStars = 5 - Math.ceil(rating);
  for (let i = 0; i < emptyStars; i++) {
    stars += '<i class="far fa-star"></i>';
  }

  return stars;
}

// Contact mentor function
function contactMentor(mentorId) {
  const mentor = mentorsData.find((m) => m.id === mentorId);
  if (mentor) {
    showNotification(
      `Ai inițiat contactul cu ${mentor.name}! Vei fi contactat în curând.`,
      "success"
    );

    // Simulate mentor contact process
    setTimeout(() => {
      showNotification(
        `${mentor.name} a fost notificat/ă de interesul tău!`,
        "info"
      );
    }, 2000);
  }
}

// Handle contact form
function handleContactForm(e) {
  e.preventDefault();

  const formData = new FormData(e.target);
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const subject = document.getElementById("subject").value;
  const message = document.getElementById("message").value;

  if (!name || !email || !subject || !message) {
    showNotification("Te rugăm să completezi toate câmpurile!", "error");
    return;
  }

  // Simulate form submission
  const submitBtn = e.target.querySelector('button[type="submit"]');
  submitBtn.innerHTML = '<span class="loading"></span> Se trimite...';
  submitBtn.disabled = true;

  setTimeout(() => {
    showNotification(
      "Mesajul a fost trimis cu succes! Îți vom răspunde în curând.",
      "success"
    );
    e.target.reset();
    submitBtn.innerHTML = "Trimite mesajul";
    submitBtn.disabled = false;
  }, 2000);
}

// Navbar scroll effect
function handleNavbarScroll() {
  const header = document.querySelector(".header");
  if (window.scrollY > 100) {
    header.style.background = "rgba(255, 255, 255, 0.95)";
    header.style.backdropFilter = "blur(10px)";
  } else {
    header.style.background = "var(--bg-white)";
    header.style.backdropFilter = "none";
  }
}

// Smooth scrolling for navigation links
function setupSmoothScrolling() {
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute("href"));
      if (target) {
        const headerHeight = document.querySelector(".header").offsetHeight;
        const targetPosition = target.offsetTop - headerHeight;

        window.scrollTo({
          top: targetPosition,
          behavior: "smooth",
        });
      }
    });
  });
}

// Animate elements on scroll
function animateOnScroll() {
  const observerOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px",
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = "1";
        entry.target.style.transform = "translateY(0)";
      }
    });
  }, observerOptions);

  // Observe elements that should animate
  document
    .querySelectorAll(".feature-card, .mentor-card, .stat")
    .forEach((el) => {
      el.style.opacity = "0";
      el.style.transform = "translateY(30px)";
      el.style.transition = "opacity 0.6s ease, transform 0.6s ease";
      observer.observe(el);
    });
}

// Notification system
function showNotification(message, type = "info") {
  // Remove existing notifications
  const existingNotifications = document.querySelectorAll(".notification");
  existingNotifications.forEach((notif) => notif.remove());

  const notification = document.createElement("div");
  notification.className = `notification notification-${type}`;
  notification.innerHTML = `
        <div class="notification-content">
            <i class="fas ${getNotificationIcon(type)}"></i>
            <span>${message}</span>
            <button class="notification-close">&times;</button>
        </div>
    `;

  // Style the notification
  notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: ${getNotificationColor(type)};
        color: white;
        padding: 1rem 1.5rem;
        border-radius: var(--border-radius);
        box-shadow: var(--shadow-lg);
        z-index: 3000;
        max-width: 400px;
        animation: slideInRight 0.3s ease;
    `;

  document.body.appendChild(notification);

  // Close button functionality
  const closeBtn = notification.querySelector(".notification-close");
  closeBtn.addEventListener("click", () => {
    notification.style.animation = "slideOutRight 0.3s ease";
    setTimeout(() => notification.remove(), 300);
  });

  // Auto remove after 5 seconds
  setTimeout(() => {
    if (notification.parentNode) {
      notification.style.animation = "slideOutRight 0.3s ease";
      setTimeout(() => notification.remove(), 300);
    }
  }, 5000);
}

function getNotificationIcon(type) {
  switch (type) {
    case "success":
      return "fa-check-circle";
    case "error":
      return "fa-exclamation-circle";
    case "warning":
      return "fa-exclamation-triangle";
    default:
      return "fa-info-circle";
  }
}

function getNotificationColor(type) {
  switch (type) {
    case "success":
      return "var(--success-color)";
    case "error":
      return "var(--error-color)";
    case "warning":
      return "var(--warning-color)";
    default:
      return "var(--primary-color)";
  }
}

// Add notification animations to CSS
const notificationStyles = document.createElement("style");
notificationStyles.textContent = `
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(100%);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes slideOutRight {
        from {
            opacity: 1;
            transform: translateX(0);
        }
        to {
            opacity: 0;
            transform: translateX(100%);
        }
    }
    
    .notification-content {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .notification-close {
        background: none;
        border: none;
        color: white;
        font-size: 1.2rem;
        cursor: pointer;
        margin-left: auto;
        padding: 0;
        width: 20px;
        height: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .notification-close:hover {
        opacity: 0.7;
    }
`;
document.head.appendChild(notificationStyles);

// Search functionality (bonus feature)
function setupSearch() {
  const searchInput = document.createElement("input");
  searchInput.type = "text";
  searchInput.placeholder = "Caută mentori...";
  searchInput.className = "search-input";

  searchInput.addEventListener("input", (e) => {
    const searchTerm = e.target.value.toLowerCase();
    const mentorCards = document.querySelectorAll(".mentor-card");

    mentorCards.forEach((card) => {
      const mentorName = card
        .querySelector(".mentor-name")
        .textContent.toLowerCase();
      const mentorSpecialty = card
        .querySelector(".mentor-specialty")
        .textContent.toLowerCase();

      if (
        mentorName.includes(searchTerm) ||
        mentorSpecialty.includes(searchTerm)
      ) {
        card.style.display = "block";
      } else {
        card.style.display = "none";
      }
    });
  });

  // Add search input to mentors section
  const mentorsSection = document.querySelector(".mentors .container");
  if (mentorsSection) {
    const searchContainer = document.createElement("div");
    searchContainer.className = "search-container";
    searchContainer.style.cssText = `
            display: flex;
            justify-content: center;
            margin-bottom: 2rem;
        `;

    searchInput.style.cssText = `
            padding: 12px 20px;
            border: 2px solid var(--border-light);
            border-radius: var(--border-radius);
            font-size: 1rem;
            width: 100%;
            max-width: 400px;
            transition: var(--transition);
        `;

    searchContainer.appendChild(searchInput);
    const filtersDiv = mentorsSection.querySelector(".mentors-filter");
    mentorsSection.insertBefore(searchContainer, filtersDiv.nextSibling);
  }
}

// Initialize search after DOM is loaded
document.addEventListener("DOMContentLoaded", function () {
  setTimeout(setupSearch, 100);
});

// Statistics counter animation
function animateCounters() {
  const counters = document.querySelectorAll(".stat-number");

  counters.forEach((counter) => {
    const target = parseInt(counter.textContent.replace(/\D/g, ""));
    const increment = target / 100;
    let current = 0;

    const timer = setInterval(() => {
      current += increment;
      if (current >= target) {
        counter.textContent = counter.textContent.replace(/\d+/, target);
        clearInterval(timer);
      } else {
        counter.textContent = counter.textContent.replace(
          /\d+/,
          Math.floor(current)
        );
      }
    }, 20);
  });
}

// Trigger counter animation when about section is visible
const aboutSection = document.querySelector(".about");
if (aboutSection) {
  const aboutObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          animateCounters();
          aboutObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.5 }
  );

  aboutObserver.observe(aboutSection);
}

// Keyboard navigation support
document.addEventListener("keydown", function (e) {
  // Close modals with Escape key
  if (e.key === "Escape") {
    const openModals = document.querySelectorAll('.modal[style*="block"]');
    openModals.forEach((modal) => closeModal(modal));
  }

  // Navigate mentors with arrow keys (when focused)
  if (document.activeElement.classList.contains("mentor-btn")) {
    const mentorCards = Array.from(document.querySelectorAll(".mentor-card"));
    const currentIndex = mentorCards.findIndex(
      (card) => card.querySelector(".mentor-btn") === document.activeElement
    );

    let nextIndex = currentIndex;

    if (e.key === "ArrowRight" || e.key === "ArrowDown") {
      nextIndex = (currentIndex + 1) % mentorCards.length;
    } else if (e.key === "ArrowLeft" || e.key === "ArrowUp") {
      nextIndex = (currentIndex - 1 + mentorCards.length) % mentorCards.length;
    }

    if (nextIndex !== currentIndex) {
      e.preventDefault();
      mentorCards[nextIndex].querySelector(".mentor-btn").focus();
    }
  }
});

// Performance optimization: Lazy loading for mentor images
function setupLazyLoading() {
  const mentorCards = document.querySelectorAll(".mentor-card");

  const imageObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("loaded");
        imageObserver.unobserve(entry.target);
      }
    });
  });

  mentorCards.forEach((card) => {
    imageObserver.observe(card);
  });
}

// Initialize lazy loading
document.addEventListener("DOMContentLoaded", setupLazyLoading);

// Dark mode toggle (bonus feature)
function setupDarkMode() {
  const darkModeToggle = document.createElement("button");
  darkModeToggle.innerHTML = '<i class="fas fa-moon"></i>';
  darkModeToggle.className = "dark-mode-toggle";
  darkModeToggle.style.cssText = `
        position: fixed;
        bottom: 20px;
        right: 20px;
        background: var(--primary-color);
        color: white;
        border: none;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        cursor: pointer;
        box-shadow: var(--shadow-lg);
        z-index: 1500;
        transition: var(--transition);
    `;

  darkModeToggle.addEventListener("click", toggleDarkMode);
  document.body.appendChild(darkModeToggle);
}

function toggleDarkMode() {
  document.body.classList.toggle("dark-mode");
  const isDark = document.body.classList.contains("dark-mode");

  const toggle = document.querySelector(".dark-mode-toggle");
  toggle.innerHTML = isDark
    ? '<i class="fas fa-sun"></i>'
    : '<i class="fas fa-moon"></i>';

  // Save preference
  localStorage.setItem("darkMode", isDark);
}

// Load dark mode preference
if (localStorage.getItem("darkMode") === "true") {
  document.body.classList.add("dark-mode");
}

// Initialize dark mode toggle
document.addEventListener("DOMContentLoaded", setupDarkMode);
