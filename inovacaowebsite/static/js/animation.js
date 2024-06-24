
    const myObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add('show');
                entry.target.classList.remove('hidden');
            } else {
                entry.target.classList.remove('show');
                entry.target.classList.add('hidden');
            }
        });
    });

    const elements = document.querySelectorAll('.hidden');

    elements.forEach((element, index) => {
        const transitionDelay = 10 + (10 * index);
        element.style.transitionDelay = `${transitionDelay}ms`;
        myObserver.observe(element);
    });




    

    const myObserverD = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add('show-d');
                entry.target.classList.remove('hidden-d');
            } else {
                entry.target.classList.remove('show-d');
                entry.target.classList.add('hidden-d');
            }
        });
    });

    const elementsD = document.querySelectorAll('.hidden-d');

    elementsD.forEach((element, index) => {
        const transitionDelay = 10 + (10 * index);
        element.style.transitionDelay = `${transitionDelay}ms`;
        myObserverD.observe(element);
    });

