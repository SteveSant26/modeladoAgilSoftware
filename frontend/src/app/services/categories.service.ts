import { Injectable, Signal, signal } from '@angular/core';

import { inject, } from '@angular/core';
import { AdapterDataService } from './adapter-data.service';
import { Category } from 'app/types';
import { tap } from 'rxjs';
import { categoryAdapter } from '@Adapters/category.adapter';
import { categoriesAdapter } from '@Adapters/categories.adapter ';

@Injectable({
  providedIn: 'root'
})
export class CategoriesService {

  private adapterDataService = inject(AdapterDataService)
  url = 'categories/'

  private _categories = signal<Category[]>([]);
  categories$ = this._categories.asReadonly();



  loadCategories() {
    this.adapterDataService.getAdaptedData<Category[]>(this.url, categoriesAdapter)
      .subscribe(categories => {this._categories.set(categories)});
  }


  getCategories(): Signal<Category[]> {
    return this.categories$
  }

  addCategory(data: Category) {
    return this.adapterDataService.postData<Category>(this.url, data, categoryAdapter).pipe(
      tap(() => this.loadCategories())
    )
  }



}
