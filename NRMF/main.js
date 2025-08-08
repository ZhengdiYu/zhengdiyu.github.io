// Navbar burger, abstract toggle, smooth anchor offset, dark mode (persisted)
document.addEventListener('DOMContentLoaded', () => {
    // Navbar burger
    const burgers = Array.from(document.querySelectorAll('.navbar-burger'));
    burgers.forEach(b => {
      b.addEventListener('click', () => {
        const target = document.getElementById(b.dataset.target);
        b.classList.toggle('is-active');
        target?.classList.toggle('is-active');
      });
    });
  
    // Abstract toggle
    const absToggle = document.getElementById('absToggle');
    const absContent = document.getElementById('absContent');
    if (absToggle && absContent){
      absToggle.addEventListener('click', () => {
        const shown = absContent.style.display !== 'none';
        absContent.style.display = shown ? 'none' : 'block';
        absToggle.querySelector('.icon').textContent = shown ? '▸' : '▾';
      });
    }
  
    // Smooth anchor scrolling with fixed-navbar offset
    const navLinks = document.querySelectorAll('a.navbar-item[href^="#"]');
    const offset = 64;
    navLinks.forEach(link => {
      link.addEventListener('click', e => {
        e.preventDefault();
        const id = link.getAttribute('href').slice(1);
        const el = document.getElementById(id);
        if (!el) return;
        const y = el.getBoundingClientRect().top + window.pageYOffset - offset;
        window.scrollTo({ top: y, behavior: 'smooth' });
      });
    });
  
    // Dark mode toggle (persist to localStorage)
    const darkBtn = document.getElementById('darkToggle');
    const root = document.documentElement;
    const saved = localStorage.getItem('nrmf-theme');
    if (saved === 'dark') root.classList.add('dark');
    darkBtn?.addEventListener('click', () => {
      root.classList.toggle('dark');
      localStorage.setItem('nrmf-theme', root.classList.contains('dark') ? 'dark' : 'light');
    });
  });
  