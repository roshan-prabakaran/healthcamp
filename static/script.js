// Flash message auto-hide
document.addEventListener("DOMContentLoaded", () => {
  const flashMessages = document.querySelectorAll(".flash-message")
  flashMessages.forEach((message) => {
    setTimeout(() => {
      message.style.display = "none"
    }, 5000)
  })
})

// Search functionality
function searchCamps() {
  const query = document.getElementById("searchQuery").value
  const location = document.getElementById("searchLocation").value

  let url = "/search?"
  if (query) url += `query=${encodeURIComponent(query)}&`
  if (location) url += `location=${encodeURIComponent(location)}&`

  window.location.href = url
}

// QR Code generation (mock implementation)
function generateQRCode(campId) {
  const modal = document.getElementById("qrModal")
  const qrCode = document.getElementById("qrCode")

  // Generate mock QR code
  const qrData = `CAMP_${campId}_USER_${Date.now()}`
  qrCode.innerHTML = `
        <div style="width: 200px; height: 200px; background: #f0f0f0; border: 2px solid #333; margin: 20px auto; display: flex; align-items: center; justify-content: center; font-family: monospace;">
            <div style="text-align: center;">
                <div style="font-size: 12px; margin-bottom: 10px;">QR CODE</div>
                <div style="font-size: 10px; word-break: break-all;">${qrData}</div>
            </div>
        </div>
        <p style="margin-top: 10px; font-size: 12px; color: #666;">
            Scan this code at the camp entrance
        </p>
    `

  modal.style.display = "block"
}

function closeQRModal() {
  document.getElementById("qrModal").style.display = "none"
}

// Close modal when clicking outside
window.onclick = (event) => {
  const modal = document.getElementById("qrModal")
  if (event.target === modal) {
    modal.style.display = "none"
  }
}

// Admin functions
function editCamp(campId) {
  alert(`Edit camp functionality would be implemented here for camp ID: ${campId}`)
}

// Form validation
function validateForm(form) {
  const inputs = form.querySelectorAll("input[required]")
  let isValid = true

  inputs.forEach((input) => {
    if (!input.value.trim()) {
      isValid = false
      input.style.borderColor = "#e74c3c"
    } else {
      input.style.borderColor = "#e1e8ed"
    }
  })

  return isValid
}

// Add form validation to all forms
document.addEventListener("DOMContentLoaded", () => {
  const forms = document.querySelectorAll("form")
  forms.forEach((form) => {
    form.addEventListener("submit", function (e) {
      if (!validateForm(this)) {
        e.preventDefault()
        alert("Please fill in all required fields.")
      }
    })
  })
})

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault()
    document.querySelector(this.getAttribute("href")).scrollIntoView({
      behavior: "smooth",
    })
  })
})

// Auto-refresh for real-time updates (mock implementation)
function enableRealTimeUpdates() {
  if (window.location.pathname === "/admin") {
    setInterval(() => {
      // In a real implementation, this would fetch updates from the server
      console.log("Checking for updates...")
    }, 30000) // Check every 30 seconds
  }
}

// Initialize real-time updates
document.addEventListener("DOMContentLoaded", enableRealTimeUpdates)

// Mobile menu toggle
function toggleMobileMenu() {
  const navMenu = document.querySelector(".nav-menu")
  navMenu.classList.toggle("active")
}

// Add mobile menu button dynamically
document.addEventListener("DOMContentLoaded", () => {
  const navbar = document.querySelector(".navbar")
  const navContainer = navbar.querySelector(".nav-container")

  if (window.innerWidth <= 768) {
    const menuToggle = document.createElement("button")
    menuToggle.innerHTML = '<i class="fas fa-bars"></i>'
    menuToggle.className = "menu-toggle"
    menuToggle.onclick = toggleMobileMenu
    navContainer.appendChild(menuToggle)
  }
})
