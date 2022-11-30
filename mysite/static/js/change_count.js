const btnMinus = document.querySelector('[data-action="minus"]');
const btnPlus = document.querySelector('[data-action="plus"]');
const count = document.querySelector('[data-counter]');

btnMinus.addEventListener('click', function () {
    if (count.innerText > 1) {
        count.innerText = Number(count.innerText) - 1
    }
})

btnPlus.addEventListener('click', function () {
    count.innerText = Number(count.innerText) + 1
})
