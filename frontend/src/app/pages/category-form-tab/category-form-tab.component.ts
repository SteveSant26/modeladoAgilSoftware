import { Component, effect, inject } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { FormComponent } from "../../components/form/form.component";
import { CategoriesService } from '@Services/categories.service';

@Component({
  selector: 'app-category-form-tab',
  imports: [FormComponent],
  templateUrl: './category-form-tab.component.html',
})
export class CategoryFormTabComponent {

  categoryFormGroup!: FormGroup;
  categoryFormFields: any;

  fb = inject(FormBuilder)
  categoriesService = inject(CategoriesService)


  constructor() {
    effect(() => {
      this.initCategoryForm()
    });
  }


  initCategoryForm() {
    this.categoryFormGroup = this.fb.group(
      {
        name: ['', [Validators.required]],
      }
    )
    this.categoryFormFields = [
      { name: 'name', type: 'text', placeholder: 'Enter the catgeory name', label: 'Category name' },
    ];
  }


  addNewCategory() {

    if (this.categoryFormGroup.valid) {
      this.categoriesService.addCategory(this.categoryFormGroup.value).subscribe()
      this.categoryFormGroup.reset()
    } 
  }

}
