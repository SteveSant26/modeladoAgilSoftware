import { Component, effect, inject, Signal } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { FormComponent } from "../../components/form/form.component";
import { CategoriesService } from '@Services/categories.service';
import { Category } from 'app/types';
import { FruitsService } from '@Services/fruits.service';
import { CustomFormValidator } from 'app/validators/noNumbers.validator';

@Component({
  selector: 'app-fruit-form-tab',
  imports: [FormComponent],
  templateUrl: './fruit-form-tab.component.html',
})
export class FruitFormTabComponent {
  fruitFormGroup!: FormGroup;
  fruitFormFields: any;
  fruitsService = inject(FruitsService);
  categoriesService = inject(CategoriesService);
  fb = inject(FormBuilder);


  categories: Signal<Category[]> = this.categoriesService.getCategories()
  selectedFruit = this.fruitsService.getSelectedFruit()


  constructor() {
    effect(() => {
      this.initFruitForm()
    });
    effect(() => {
      const fruit = this.selectedFruit();
      if (fruit) {
        this.fruitFormGroup?.patchValue({
          name: fruit.name,
          price: fruit.price,
          category_id: fruit.category.id
        });
      }
    })
  }


  ngOnInit() {
    this.categoriesService.loadCategories()
  }

  initFruitForm() {
    this.fruitFormGroup = this.fb.group({
      name: ['', [Validators.required, CustomFormValidator.noNumbers]],
      price: [0, [Validators.required, Validators.min(0.05)]],
      category_id: [null, [Validators.required]],
    });

    this.fruitFormFields = [
      { name: 'name', type: 'text', placeholder: 'Enter the fruit name', label: 'Name' },
      { name: 'price', type: 'number', placeholder: 'Enter the fruit price', label: 'Price' },
      {
        name: 'category_id',
        type: 'select',
        placeholder: 'Select a category',
        label: 'Category',
        options: this.categories().map(category => ({
          value: category.id,
          label: category.name,
        })),
      },
    ];
  }


  addUpdateFruit() {
    if (this.fruitFormGroup.valid) {
      let fruit = this.fruitFormGroup.value
      if (this.selectedFruit()) {
        fruit.id = this.selectedFruit()?.id
        this.fruitsService.updateFruit(fruit).subscribe()
      }
      else {
        this.fruitsService.addFruit(this.fruitFormGroup.value).subscribe()
      }
      this.fruitFormGroup.reset()
      this.fruitsService.selectFruit(null)
    }

  }
}
