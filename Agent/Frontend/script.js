


const SearchButton = document.querySelector('.complain-section input[type="button"]');
const inputField = document.querySelector('.complain-section input[type="text"]');




async function getInput(inputField) {
    const input = inputField.value;
    return input;
}
// http://127.0.0.1:5500/Agent/Frontend/index.html
async function SendData(question) {
    const response = await fetch('http://127.0.0.1:8000/ask', {

    })    
}

SearchButton.addEventListener('click', async () => {
   const input = await getInput(inputField);
   console.log(input);
});
