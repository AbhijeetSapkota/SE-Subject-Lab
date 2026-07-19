// Frontend logic for dynamic interactions

document.addEventListener('DOMContentLoaded', () => {
    // Flash message auto-hide
    const flashMessages = document.querySelectorAll('.flash');
    if (flashMessages.length > 0) {
        setTimeout(() => {
            flashMessages.forEach(msg => {
                msg.style.opacity = '0';
                setTimeout(() => msg.remove(), 300);
            });
        }, 5000);
    }
});
