import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms'; // Import FormsModule pour ngModel

@Component({
  selector: 'app-page-resultat-recherche',
  standalone: true,
  imports: [CommonModule, FormsModule], // Inclure FormsModule ici
  templateUrl: './page-resultat-recherche.component.html',
  styleUrls: ['./page-resultat-recherche.component.scss']
})
export class PageResultatRechercheComponent {
  // Liste des résultats
  results = [
    {
      destination: 'Madrid',
      price: 41,
      transport: 'Train',
      carbonFootprint: '2.93 g de CO2 par km',
      duration: 300,
      travelClass: 'Classe économique',
      image: 'assets/madrid1.jpg',
    },
    {
      destination: 'Madrid',
      price: 135,
      transport: 'Avion',
      carbonFootprint: '188 g de CO2 par km',
      duration: 120,
      travelClass: 'Classe business',
      image: 'assets/madrid2.jpg',
    },
    {
      destination: 'Madrid',
      price: 41,
      transport: 'Bus',
      carbonFootprint: '218 g de CO2 par km',
      duration: 480,
      travelClass: 'Classe économique',
      image: 'assets/madrid3.jpg',
    },
    {
      destination: 'Madrid',
      price: 50,
      transport: 'Covoiturage',
      carbonFootprint: '100 g de CO2 par km',
      duration: 400,
      travelClass: 'Classe économique',
      image: 'assets/madrid4.jpg',
    },
    {
      destination: 'Madrid',
      price: 200,
      transport: 'Marin',
      carbonFootprint: '300 g de CO2 par km',
      duration: 600,
      travelClass: 'Classe business',
      image: 'assets/madrid5.jpg',
    },
  ];

  // Filtres sélectionnés
  selectedClass: string = 'Toutes les classes';
  selectedTransport: string[] = [];
  sortCriteria: string = ''; // Critère de tri

  // Méthode pour appliquer les filtres et le tri
  getFilteredResults() {
    let filteredResults = this.results.filter((result) => {
      // Filtrer par classe
      const classFilter = this.selectedClass === 'Toutes les classes' || result.travelClass === this.selectedClass;

      // Filtrer par moyen de transport
      const transportFilter =
        this.selectedTransport.length === 0 || this.selectedTransport.includes(result.transport);

      return classFilter && transportFilter;
    });

    // Appliquer le tri
    if (this.sortCriteria === 'eco') {
      filteredResults.sort((a, b) => parseFloat(a.carbonFootprint) - parseFloat(b.carbonFootprint));
    } else if (this.sortCriteria === 'price') {
      filteredResults.sort((a, b) => a.price - b.price);
    } else if (this.sortCriteria === 'duration') {
      filteredResults.sort((a, b) => a.duration - b.duration);
    }

    return filteredResults;
  }

  // Méthode pour trier les résultats
  sortBy(criteria: string) {
    this.sortCriteria = criteria; // Enregistre le critère sélectionné
  }

  // Méthode pour gérer les changements des filtres
  toggleTransportFilter(transport: string) {
    if (this.selectedTransport.includes(transport)) {
      this.selectedTransport = this.selectedTransport.filter((t) => t !== transport);
    } else {
      this.selectedTransport.push(transport);
    }
  }
}
