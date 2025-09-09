window.addEventListener('scroll', function() {
    const headerInner = document.querySelector('.header-inner'); // Seleccionamos el inner
    const headerHeight = headerInner.offsetHeight; // Usamos la altura del inner
    const scrollPosition = window.scrollY;
    const body = document.body;

    // Solo añadimos la clase 'sticky' al contenedor padre '.header'
    const headerOuter = document.querySelector('.header'); 

    if (scrollPosition > headerHeight) { // Comprobamos si hemos superado la altura original del header
        headerOuter.classList.add('sticky');
        // Añadimos padding-top al body para evitar que el contenido quede oculto
        body.style.paddingTop = headerHeight + 'px'; 
    } else {
        headerOuter.classList.remove('sticky');
        body.style.paddingTop = '0'; // Restauramos el padding
    }
});

//IMG SLIDER
document.addEventListener('DOMContentLoaded', () => {
    const slider = document.querySelector('.slider');
    const navDots = document.querySelectorAll('.nav-dot');
    const slides = document.querySelectorAll('.slide');
    const slideWidth = slides[0].clientWidth;
    let currentSlide = 0;

    // Función para cambiar a la siguiente diapositiva
    const goToNextSlide = () => {
        currentSlide = (currentSlide + 1) % slides.length;
        slider.scrollLeft = currentSlide * slideWidth;

        // Actualiza los puntos de navegación
        navDots.forEach(d => d.classList.remove('active'));
        navDots[currentSlide].classList.add('active');
    };

    // Configura el intervalo de tiempo para el cambio automático (5000 ms = 5 segundos)
    setInterval(goToNextSlide, 5000);

    // Opcional: Para evitar que el carrusel se mueva automáticamente si el usuario interactúa
    // con él, puedes limpiar el intervalo y reiniciarlo.

    // ... (Tu código existente para botones o scroll manual aquí) ...
});