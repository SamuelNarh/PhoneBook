const mobile_format = document.querySelector(".mobile_format");

function formatPhoneNumber(value) {
  const phoneNumber = value.replace(/[^\d]/g, "");
  const phoneNumberLength = phoneNumber.length;
  if (phoneNumber<4) 
   {return phoneNumber.slice(0,4) ;}
  if (phoneNumberLength <7) {
  return  `${phoneNumber.slice(0, 3)}-${phoneNumber.slice(3)}`;
  }
  return `${phoneNumber.slice(0, 3)}-${phoneNumber.slice(3,6,)}-${phoneNumber.slice(6,10)}`;
}

function phoneNumberFormatter() {
  const inputField = document.querySelector(".mobile_format");
  const formattedInputValue = formatPhoneNumber(inputField.value);
  inputField.value = formattedInputValue;
}

mobile_format.addEventListener('input',phoneNumberFormatter)