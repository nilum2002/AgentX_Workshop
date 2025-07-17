


const SearchButton = document.querySelector('.complain-section input[type="button"]');
const inputField = document.querySelector('.complain-section input[type="text"]');




async function getInput(inputField) {
    const input = inputField.value;
    return input;
}

SearchButton.addEventListener('click', async () => {
   const input = await getInput(inputField);
   console.log(input);
});
