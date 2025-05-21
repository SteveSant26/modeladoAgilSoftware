import { Component, inject, input, output } from '@angular/core';
import { FormBuilder, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatSelectModule } from '@angular/material/select';

import { ErrorHandler } from 'app/utils/error-handler';

@Component({
  selector: 'app-form',
  imports: [FormsModule, ReactiveFormsModule, MatFormFieldModule, MatInputModule, MatSelectModule],
  templateUrl: './form.component.html',
  styleUrl: './form.component.css'
})
export class FormComponent {
  formTitle = input.required<string>()
  formGroup =  input.required<FormGroup>()
  formFields = input.required<any>()



  sendForm = output<any>()




  getErrorMessage(controlName: string): string | null {
    return ErrorHandler.getErrorMessage(this.formGroup(), controlName)
  }
}
