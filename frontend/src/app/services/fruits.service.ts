import { inject, Injectable, signal, effect, Signal } from '@angular/core';

import { tap } from 'rxjs';
import { AdapterDataService } from './adapter-data.service';
import { Fruit } from 'app/types';
import { fruitAdapter } from '@Adapters/fruit.adapter';
import { fruitsAdapter } from '@Adapters/fruits.adapter';

@Injectable({
  providedIn: 'root'
})
export class FruitsService {
  private adapterDataService = inject(AdapterDataService);
  private url = 'fruits/';

  private _fruits = signal<Fruit[]>([]);
  fruits$ = this._fruits.asReadonly();


  private selectedFruit = signal<Fruit | null>(null);

  selectFruit(fruit: Fruit | null) {
    this.selectedFruit.set(fruit)
  }

  getSelectedFruit() {
    return this.selectedFruit
  }



  loadFruits() {
    this.adapterDataService.getAdaptedData<Fruit[]>(this.url, fruitsAdapter)
      .subscribe(fruits => this._fruits.set(fruits));
  }

  getFruits(): Signal<Fruit[]> {
    return this.fruits$;
  }

  addFruit(data: Fruit) {
    return this.adapterDataService.postData<Fruit>(this.url, data, fruitAdapter).pipe(
      tap(() => this.loadFruits())
    );
  }

  updateFruit(data: Fruit) {
    return this.adapterDataService.updateData<Fruit>(this.url + data.id, data, fruitAdapter).pipe(
      tap(() => this.loadFruits())
    );
  }

  deleteFruit(fruitId: number) {
    return this.adapterDataService.deleteData<Fruit>(this.url + fruitId, fruitAdapter).pipe(
      tap(() => this.loadFruits())
    );
  }
}
