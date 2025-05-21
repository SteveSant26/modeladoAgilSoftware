import { Component, inject, OnInit, Signal } from '@angular/core';
import { MatIconModule } from '@angular/material/icon';
import { MatListModule } from '@angular/material/list';
import { FruitsService } from '@Services/fruits.service';
import { Fruit } from 'app/types';


@Component({
  selector: 'app-fruit-list',
  imports: [MatListModule, MatIconModule],
  templateUrl: './fruit-list.component.html',
})
export class FruitListComponent implements OnInit {

  fruitsService = inject(FruitsService)
  fruits: Signal<Fruit[]> = this.fruitsService.getFruits(); 


  ngOnInit() {
    this.fruitsService.loadFruits(); 
  }

  deleteFruit(fruitId: number) {
    this.fruitsService.deleteFruit(fruitId).subscribe()
  }

}
