import { Component, inject } from '@angular/core';
import { MatTabsModule } from '@angular/material/tabs';
import { FruitFormTabComponent } from "../fruit-form-tab/fruit-form-tab.component";
import { CategoryFormTabComponent } from "../category-form-tab/category-form-tab.component";
import { FruitListComponent } from "../../components/fruit-list/fruit-list.component";

@Component({
  selector: 'app-main-page',
  imports: [MatTabsModule, FruitFormTabComponent, CategoryFormTabComponent, FruitListComponent],
  templateUrl: './main.component.html',
})
export class MainComponent {





}
