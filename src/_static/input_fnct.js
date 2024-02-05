window.onload = () => {
    setTimeout(function() {
        var tableElements = document.querySelectorAll('.dataTables_wrapper');
        if (tableElements.length > 0) {
            tableElements.forEach(tableElement => {
                var inputElement = tableElement.querySelector('.dataTables_filter input');
                var allTagButtons = tableElement.querySelectorAll('.btn');
                inputElement.addEventListener('input', () => {
                    var inputValue = inputElement.value;
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
                allTagButtons.forEach(btn => {
                    btn.onclick = function() { insertText(btn, inputElement) };
                });
            })
        } else {
            console.log('No input elements found.');
        }
    }, 1000);
};
