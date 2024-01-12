window.onload = () => {
    // console.log('Window loaded.')
    setTimeout(function() {
        var inputElement = document.querySelector('.dataTables_wrapper .dataTables_filter input');
        var allTagButtons = document.querySelectorAll('.btn');
        if (inputElement) {
            inputElement.addEventListener('input', () => {
                var inputValue = inputElement.value;
                // console.log('Input value: ' + inputValue);

                allTagButtons.forEach(btn => {
                    if (inputValue.includes(btn.textContent)) {
                        if (btn.classList.contains('btn-light')) {
                            btn.classList.remove('btn-light');
                            btn.classList.add('btn-secondary');
                        }
                    } else {
                        if (btn.classList.contains('btn-secondary')) {
                            btn.classList.remove('btn-secondary');
                            btn.classList.add('btn-light');
                        }
                    };
                });

            });
        } else {
            console.log('Note: Input element not found.');
        }
    }, 1000);
};

