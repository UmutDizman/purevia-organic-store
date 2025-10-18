const reduceMotion = window.matchMedia('prefer-reduced-motion: reduce').matches;
const target = document.querySelectorAll(' [data-revial], .revial, .card ');



if( reduceMotion || !('IntersectionObserver' in window)) {
    target.forEach(el => el.classList.add('show'));
}
    else {
        const io = new IntersectionObserver((entries, obs) => {
            entries.forEach(entry => {
                if (!entry.isIntersecting) return;

                const el = entry.target;


                const delay = parseInt(el.getAttribute('data-delay') || '0',10);
                if (delay) el.style.transitionDelay = ${delay}ms;

                el.classList.add('show');
                obs.unobserve(el);
            });
        },{
            threshold:0.15,
            rootMargin:'0px 0px -5% 0px'

        });


        targets.forEach((el, i) => {

            if (el.matches('.card')) el.setAttribute('data-delay', (i % 10) * 50);
            el.classList.add('reveal');

        });
    }