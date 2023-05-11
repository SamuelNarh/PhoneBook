

const mobile_format =document.querySelector('.mobile_format');
console.log(mobile_format)
const phone_number = function(){

    if (mobile_format.value.length ===3|| mobile_format.value.length ===7)
    {
        mobile_format.value+="-";
    }
}
mobile_format.addEventListener('input',phone_number);
