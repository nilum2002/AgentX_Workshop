


const SearchButton = document.querySelector('.complain-section input[type="button"]');
const inputField = document.querySelector('.complain-section input[type="text"]');
const responseField = document.querySelector('.response p');




async function getInput(inputField) {
    const input = inputField.value;
    return input;
}
// http://127.0.0.1:5500/Agent/Frontend/index.html
async function SendData(question) {
    const response = await fetch('http://127.0.0.1:8000/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: question })
    })
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }else{
        const data = await response.json();
        
    
        console.log(data);
        return data.response;
    }
    }



SearchButton.addEventListener('click', async () => {
   const input = await getInput(inputField);
   const res = await SendData(input);
   console.log(res);
   responseField.textContent = res;
});
