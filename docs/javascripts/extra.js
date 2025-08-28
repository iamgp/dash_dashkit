// Custom JavaScript for Dashkit documentation

document.addEventListener('DOMContentLoaded', function() {
    // Add copy to clipboard functionality for code blocks
    const codeBlocks = document.querySelectorAll('pre code');
    
    codeBlocks.forEach((block, index) => {
        const button = document.createElement('button');
        button.className = 'copy-button';
        button.innerHTML = '📋';
        button.title = 'Copy to clipboard';
        button.style.cssText = `
            position: absolute;
            top: 8px;
            right: 8px;
            background: rgba(255,255,255,0.8);
            border: none;
            border-radius: 4px;
            padding: 4px 8px;
            cursor: pointer;
            font-size: 12px;
            opacity: 0;
            transition: opacity 0.2s;
        `;
        
        // Make parent relative for absolute positioning
        block.parentElement.style.position = 'relative';
        
        // Show button on hover
        block.parentElement.addEventListener('mouseenter', () => {
            button.style.opacity = '1';
        });
        
        block.parentElement.addEventListener('mouseleave', () => {
            button.style.opacity = '0';
        });
        
        // Copy functionality
        button.addEventListener('click', () => {
            navigator.clipboard.writeText(block.textContent).then(() => {
                button.innerHTML = '✅';
                button.style.background = 'rgba(76, 175, 80, 0.8)';
                setTimeout(() => {
                    button.innerHTML = '📋';
                    button.style.background = 'rgba(255,255,255,0.8)';
                }, 2000);
            });
        });
        
        block.parentElement.appendChild(button);
    });
    
    // Add smooth scrolling for anchor links
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    anchorLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            const targetId = link.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                e.preventDefault();
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
                
                // Update URL
                history.pushState(null, null, `#${targetId}`);
            }
        });
    });
    
    // Enhance table responsiveness
    const tables = document.querySelectorAll('.md-typeset table:not([class])');
    tables.forEach(table => {
        const wrapper = document.createElement('div');
        wrapper.style.cssText = 'overflow-x: auto; margin: 1em 0;';
        table.parentNode.insertBefore(wrapper, table);
        wrapper.appendChild(table);
    });
    
    // Add "Back to top" functionality
    const backToTop = document.createElement('button');
    backToTop.innerHTML = '↑';
    backToTop.className = 'back-to-top';
    backToTop.style.cssText = `
        position: fixed;
        bottom: 20px;
        right: 20px;
        background: #448aff;
        color: white;
        border: none;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        font-size: 20px;
        cursor: pointer;
        opacity: 0;
        transition: opacity 0.3s;
        z-index: 1000;
        box-shadow: 0 2px 10px rgba(0,0,0,0.2);
    `;
    
    document.body.appendChild(backToTop);
    
    // Show/hide back to top button
    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) {
            backToTop.style.opacity = '1';
        } else {
            backToTop.style.opacity = '0';
        }
    });
    
    // Back to top functionality
    backToTop.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
    
    // Enhance code syntax highlighting for Python
    const pythonBlocks = document.querySelectorAll('code.language-python');
    pythonBlocks.forEach(block => {
        // Add data attribute for better styling
        block.setAttribute('data-lang', 'python');
    });
    
    // Add external link icons
    const externalLinks = document.querySelectorAll('a[href^="http"]:not([href*="your-domain.com"])');
    externalLinks.forEach(link => {
        if (!link.querySelector('svg') && !link.textContent.includes('GitHub')) {
            link.innerHTML += ' <svg style="width: 12px; height: 12px; display: inline; margin-left: 2px;" viewBox="0 0 24 24"><path fill="currentColor" d="M14,3V5H17.59L7.76,14.83L9.17,16.24L19,6.41V10H21V3M19,19H5V5H12V3H5C3.89,3 3,3.9 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V12H19V19Z" /></svg>';
        }
    });
});

// Add keyboard navigation enhancement
document.addEventListener('keydown', function(e) {
    // Ctrl/Cmd + K to focus search
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        const searchInput = document.querySelector('.md-search__input');
        if (searchInput) {
            searchInput.focus();
        }
    }
});

// Analytics and tracking (placeholder)
function trackPageView(page) {
    // Add your analytics tracking here
    console.log('Page view:', page);
}

// Track initial page load
trackPageView(window.location.pathname);