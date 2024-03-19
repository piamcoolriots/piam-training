export const EmailValidation = (value) => {
    let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    let isEmail = emailRegex.test(value);
    if(!isEmail) {
        return "Invalid email address";
    }
    return "";
}