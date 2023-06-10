
window.addEventListener('DOMContentLoaded', () => {
    const counterElement = document.querySelector('.counter');
    const uploadInput = document.getElementById('img');
    let count = 0;
  
    uploadInput.addEventListener('change', (event) => {
      const files = event.target.files;
      count += files.length;
      counterElement.textContent = count;
    });
  });