// Main JavaScript file for P R Pote Patil College Website

document.addEventListener('DOMContentLoaded', function() {
    
    // Initialize tooltips
    initializeTooltips();
    
    // Initialize search functionality
    initializeSearch();
    
    // Initialize dynamic loading states
    initializeLoadingStates();
    
    // Initialize scroll to top button
    initializeScrollToTop();
    
    // Initialize responsive table handling
    initializeResponsiveTables();
    
    // Initialize filter functionality
    initializeFilters();
    
    // Initialize form validation
    initializeFormValidation();
    
    // Initialize lazy loading for images
    initializeLazyLoading();
});

/**
 * Initialize Bootstrap tooltips
 */
function initializeTooltips() {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

/**
 * Enhanced search functionality
 */
function initializeSearch() {
    const searchForm = document.querySelector('form[action*="search"]');
    const searchInput = document.querySelector('input[name="q"]');
    
    if (searchForm && searchInput) {
        // Add search suggestions (placeholder for future enhancement)
        searchInput.addEventListener('input', debounce(function(e) {
            const query = e.target.value.trim();
            if (query.length > 2) {
                // Future: Implement search suggestions
                console.log('Search query:', query);
            }
        }, 300));
        
        // Prevent empty searches
        searchForm.addEventListener('submit', function(e) {
            if (searchInput.value.trim().length === 0) {
                e.preventDefault();
                showAlert('Please enter a search term', 'warning');
            }
        });
    }
}

/**
 * Initialize loading states for dynamic content
 */
function initializeLoadingStates() {
    const loadingButtons = document.querySelectorAll('.btn[data-loading]');
    
    loadingButtons.forEach(button => {
        button.addEventListener('click', function() {
            showLoading(this);
            // Simulate loading (remove in production with actual async operations)
            setTimeout(() => {
                hideLoading(this);
            }, 2000);
        });
    });
}

/**
 * Initialize scroll to top functionality
 */
function initializeScrollToTop() {
    // Create scroll to top button
    const scrollButton = document.createElement('button');
    scrollButton.innerHTML = '<i class="fas fa-arrow-up"></i>';
    scrollButton.className = 'btn btn-primary scroll-to-top';
    scrollButton.style.cssText = `
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 1000;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        display: none;
        box-shadow: 0 2px 10px rgba(0,0,0,0.3);
    `;
    
    document.body.appendChild(scrollButton);
    
    // Show/hide on scroll
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            scrollButton.style.display = 'block';
        } else {
            scrollButton.style.display = 'none';
        }
    });
    
    // Smooth scroll to top
    scrollButton.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

/**
 * Initialize responsive table handling
 */
function initializeResponsiveTables() {
    const tables = document.querySelectorAll('.table-responsive table');
    
    tables.forEach(table => {
        // Add mobile-friendly table scrolling indicator
        const wrapper = table.closest('.table-responsive');
        if (wrapper) {
            wrapper.addEventListener('scroll', function() {
                const isAtStart = this.scrollLeft === 0;
                const isAtEnd = this.scrollLeft >= (this.scrollWidth - this.clientWidth);
                
                // Add visual indicators for scroll availability
                wrapper.classList.toggle('scroll-start', isAtStart);
                wrapper.classList.toggle('scroll-end', isAtEnd);
            });
        }
    });
}

/**
 * Initialize filter functionality
 */
function initializeFilters() {
    const filterSelects = document.querySelectorAll('select[id*="Filter"]');
    
    filterSelects.forEach(select => {
        select.addEventListener('change', function() {
            const filterId = this.id;
            const filterValue = this.value.toLowerCase();
            
            // Generic filter function for various pages
            filterContent(filterId, filterValue);
        });
    });
}

/**
 * Generic content filtering function
 */
function filterContent(filterId, filterValue) {
    let targetElements = [];
    
    // Determine target elements based on filter type
    if (filterId.includes('course')) {
        targetElements = document.querySelectorAll('.course-item, tr');
    } else if (filterId.includes('department')) {
        targetElements = document.querySelectorAll('.faculty-card, .department-item');
    } else if (filterId.includes('subject')) {
        targetElements = document.querySelectorAll('.paper-card, .subject-item');
    }
    
    targetElements.forEach(element => {
        if (!filterValue || element.textContent.toLowerCase().includes(filterValue)) {
            element.style.display = '';
        } else {
            element.style.display = 'none';
        }
    });
    
    // Update results count
    updateResultsCount(targetElements, filterValue);
}

/**
 * Update results count after filtering
 */
function updateResultsCount(elements, filterValue) {
    const visibleCount = Array.from(elements).filter(el => el.style.display !== 'none').length;
    
    // Find or create results counter
    let counter = document.querySelector('.results-count');
    if (!counter) {
        counter = document.createElement('div');
        counter.className = 'results-count alert alert-info';
        const container = document.querySelector('.container');
        if (container) {
            container.insertBefore(counter, container.firstChild);
        }
    }
    
    if (filterValue) {
        counter.textContent = `Showing ${visibleCount} results`;
        counter.style.display = 'block';
    } else {
        counter.style.display = 'none';
    }
}

/**
 * Initialize form validation
 */
function initializeFormValidation() {
    const forms = document.querySelectorAll('form[data-validate]');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!validateForm(this)) {
                e.preventDefault();
            }
        });
    });
}

/**
 * Basic form validation
 */
function validateForm(form) {
    let isValid = true;
    const requiredFields = form.querySelectorAll('[required]');
    
    requiredFields.forEach(field => {
        if (!field.value.trim()) {
            isValid = false;
            field.classList.add('is-invalid');
            showFieldError(field, 'This field is required');
        } else {
            field.classList.remove('is-invalid');
            hideFieldError(field);
        }
    });
    
    return isValid;
}

/**
 * Show field validation error
 */
function showFieldError(field, message) {
    let errorDiv = field.nextElementSibling;
    if (!errorDiv || !errorDiv.classList.contains('invalid-feedback')) {
        errorDiv = document.createElement('div');
        errorDiv.className = 'invalid-feedback';
        field.parentNode.insertBefore(errorDiv, field.nextSibling);
    }
    errorDiv.textContent = message;
}

/**
 * Hide field validation error
 */
function hideFieldError(field) {
    const errorDiv = field.nextElementSibling;
    if (errorDiv && errorDiv.classList.contains('invalid-feedback')) {
        errorDiv.remove();
    }
}

/**
 * Initialize lazy loading for images
 */
function initializeLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');
    
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    imageObserver.unobserve(img);
                }
            });
        });
        
        images.forEach(img => imageObserver.observe(img));
    } else {
        // Fallback for browsers without IntersectionObserver
        images.forEach(img => {
            img.src = img.dataset.src;
        });
    }
}

/**
 * Show loading state on button
 */
function showLoading(button) {
    const originalText = button.innerHTML;
    button.dataset.originalText = originalText;
    button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Loading...';
    button.disabled = true;
}

/**
 * Hide loading state on button
 */
function hideLoading(button) {
    button.innerHTML = button.dataset.originalText || button.innerHTML;
    button.disabled = false;
}

/**
 * Show alert message
 */
function showAlert(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    const container = document.querySelector('.container');
    if (container) {
        container.insertBefore(alertDiv, container.firstChild);
        
        // Auto-hide after 5 seconds
        setTimeout(() => {
            alertDiv.remove();
        }, 5000);
    }
}

/**
 * Debounce function for performance optimization
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * Format date for display
 */
function formatDate(date, options = {}) {
    const defaultOptions = {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    };
    
    return new Date(date).toLocaleDateString('en-IN', { ...defaultOptions, ...options });
}

/**
 * Format time for display
 */
function formatTime(time) {
    return new Date(`2000-01-01 ${time}`).toLocaleTimeString('en-IN', {
        hour: '2-digit',
        minute: '2-digit',
        hour12: true
    });
}

/**
 * Copy text to clipboard
 */
function copyToClipboard(text) {
    if (navigator.clipboard) {
        navigator.clipboard.writeText(text).then(() => {
            showAlert('Copied to clipboard!', 'success');
        });
    } else {
        // Fallback for older browsers
        const textArea = document.createElement('textarea');
        textArea.value = text;
        document.body.appendChild(textArea);
        textArea.select();
        document.execCommand('copy');
        document.body.removeChild(textArea);
        showAlert('Copied to clipboard!', 'success');
    }
}

/**
 * Handle network errors gracefully
 */
function handleNetworkError(error) {
    console.error('Network error:', error);
    showAlert('Network error. Please check your connection and try again.', 'danger');
}

/**
 * Initialize dark mode toggle (if needed in future)
 */
function initializeDarkMode() {
    const darkModeToggle = document.querySelector('#darkModeToggle');
    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', function() {
            document.body.classList.toggle('dark-mode');
            localStorage.setItem('darkMode', document.body.classList.contains('dark-mode'));
        });
        
        // Load saved preference
        if (localStorage.getItem('darkMode') === 'true') {
            document.body.classList.add('dark-mode');
        }
    }
}

// Export functions for use in other scripts
window.CollegeApp = {
    showAlert,
    showLoading,
    hideLoading,
    copyToClipboard,
    formatDate,
    formatTime,
    debounce
};
