const myForms = document.querySelectorAll('.myForm');
        myForms.forEach(form => {
            form.addEventListener('submit', (event) => {
                event.preventDefault();

                const accordion = document.getElementById('myAccordion');
                const accordionState = [];
                const accordionItems = accordion.querySelectorAll('.accordion-item');
                accordionItems.forEach((item, index) => {
                    const isExpanded = item.querySelector('.accordion-collapse').classList.contains('show');
                    accordionState[index] = isExpanded;
                });
                localStorage.setItem('accordionState', JSON.stringify(accordionState));

                location.reload();
            });
        });

        const savedAccordionState = JSON.parse(localStorage.getItem('accordionState'));
        if (savedAccordionState) {
            const accordionItems = document.querySelectorAll('.accordion-item');
            accordionItems.forEach((item, index) => {
                if (savedAccordionState[index]) {
                    item.querySelector('.accordion-collapse').classList.add('show');
                }
            });
        }