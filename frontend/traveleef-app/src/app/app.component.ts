import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { InscriptionComponent } from "./inscription/inscription.component";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, InscriptionComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'traveleef-app';
}
