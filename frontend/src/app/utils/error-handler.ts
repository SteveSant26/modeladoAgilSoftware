import { FormGroup } from "@angular/forms";
import { retry } from "rxjs";


export class ErrorHandler {

  static getErrorMessage(form: FormGroup, controlName: string): string | null {
    const control = form.get(controlName);

    if (control && (control.touched || control.dirty) && control.invalid) {
      if (control.hasError('required')) {
        return 'This field is required.';
      }
      if (control.hasError('minlength')) {
        return `Minimum length is ${control.getError('minlength').requiredLength} characters.`;
      }
      if (control.hasError('min')) {
        return 'Value must be greater than 0.';
      }
      'This field cannot contain numbers.';
      if (control.hasError('noNumbers')) {
        return 'No numbers allowed'
      }
    }

    return null;
  }
}
