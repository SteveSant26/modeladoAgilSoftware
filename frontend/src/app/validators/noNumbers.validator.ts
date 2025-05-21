import { AbstractControl, ValidationErrors } from '@angular/forms';


export class CustomFormValidator {
    static noNumbers(control: AbstractControl): ValidationErrors | null {
        const value = control.value;
        const hasNumbers = /\d/.test(value);
        return hasNumbers ? { noNumbers: true } : null;
    }
}