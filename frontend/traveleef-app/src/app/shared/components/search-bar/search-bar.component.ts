import { Component } from '@angular/core';
import {FormBuilder, FormGroup, FormsModule, ReactiveFormsModule, Validators} from "@angular/forms";
import {NgForOf, NgIf} from "@angular/common";
import {Router} from "@angular/router";

@Component({
  selector: 'app-search-bar',
  standalone: true,
  imports: [
    FormsModule,
    NgForOf,
    NgIf,
    ReactiveFormsModule
  ],
  templateUrl: './search-bar.component.html',
  styleUrl: './search-bar.component.scss'
})
export class SearchBarComponent {

  searchForm: FormGroup;

  nombreVoyageurs = {
    adulte: 1,
    enfant: 0,
    bebe: 0
  };

  constructor(private fb: FormBuilder, private router: Router) {
    this.searchForm = this.fb.group({
      departureId: ['', Validators.required],
      arrivalId: ['', Validators.required],
      outboundDate: ['', Validators.required],
      returnDate: [''],
      tripType: ['',Validators.required],
    });
  }

  // Fonction permettant d'incrémenter ou décrémenter le nombre de voyageur.
  modifierNombreVoyageurs(type: 'adulte' | 'enfant' | 'bebe', valeur: number): void {
    const nouvelleValeur = this.nombreVoyageurs[type] + valeur;
    if (nouvelleValeur >= 0) {
      this.nombreVoyageurs[type] = nouvelleValeur;
    }
  }

  onSearch(): void {
    console.log("Entre");
    if (this.searchForm.valid) {
      const formData = this.searchForm.value;

      const apiData = {
        departure_id: formData.departureId,
        arrival_id: formData.arrivalId,
        outbound_date: formData.outboundDate,
        return_date: formData.returnDate || null,
        trip_type: formData.tripType,
        adults: this.nombreVoyageurs.adulte,
        children: this.nombreVoyageurs.enfant,
        infants: this.nombreVoyageurs.bebe
      };
      console.log(apiData);
      this.router.navigate(['/resultats'], { state: { data: apiData } });
    } else {
      console.log("Formulaire invalide");
    }
  }
}
