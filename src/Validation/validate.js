import { EmailValidation } from "./EmailValidation";

function Validate(type, value) {
    if(type === 'email') {
        EmailValidation(value);
    }

}

export default Validate;