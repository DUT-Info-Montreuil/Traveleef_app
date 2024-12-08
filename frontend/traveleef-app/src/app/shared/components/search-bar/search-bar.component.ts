import { Component } from '@angular/core';
import {FormsModule} from "@angular/forms";
import {NgForOf, NgIf} from "@angular/common";

@Component({
  selector: 'app-search-bar',
  standalone: true,
  imports: [
    FormsModule,
    NgForOf,
    NgIf
  ],
  templateUrl: './search-bar.component.html',
  styleUrl: './search-bar.component.scss'
})
export class SearchBarComponent {

  nombreVoyageurs = {
    adulte: 1,
    enfant: 0,
    bebe: 0
  };

  // Fonction permettant d'incrémenter ou décrémenter le nombre de voyageur.
  modifierNombreVoyageurs(type: 'adulte' | 'enfant' | 'bebe', valeur: number): void {
    const nouvelleValeur = this.nombreVoyageurs[type] + valeur;
    if (nouvelleValeur >= 0) {
      this.nombreVoyageurs[type] = nouvelleValeur;
    }
  }

  onSearch(): void {
    console.log("data");
  }

}
