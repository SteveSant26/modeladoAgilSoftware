import { Component } from '@angular/core';
import { NavbarComponent } from "@Components/navbar/navbar.component";
import { MainComponent } from "@Pages/main/main.component";

@Component({
  selector: 'app-root',
  imports: [NavbarComponent, MainComponent],
  templateUrl: './app.component.html',
})
export class AppComponent {
}
