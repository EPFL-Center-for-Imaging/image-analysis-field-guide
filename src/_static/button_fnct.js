function insertText(button, inputElement) {
    var buttonText = button.textContent;

    if (button.classList.contains('btn-light')) {
        // Append the button text to the input
        inputElement.value += ' ' + buttonText + ' ';
    } else {
        // Remove the button text from the input
        inputElement.value = inputElement.value.replace(new RegExp(buttonText, 'g'), '');
        inputElement.value = inputElement.value.replace(/ +/g, ' ');
    }

    // Trigger the input event
    var event = new Event('input', { bubbles: true, cancelable: true });
    inputElement.dispatchEvent(event);
}