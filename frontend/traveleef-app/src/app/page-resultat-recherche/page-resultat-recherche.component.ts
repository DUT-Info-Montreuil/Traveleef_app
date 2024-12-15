import { Component } from '@angular/core';
import { CommonModule, NgOptimizedImage } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-page-resultat-recherche',
  standalone: true,
  imports: [CommonModule, FormsModule, NgOptimizedImage],
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
      image: 'assets/LogoTexte_Traveleef_N.png',
      link: 'https://example.com/train-madrid'
    },
    {
      destination: 'Madrid',
      price: 135,
      transport: 'Avion',
      carbonFootprint: '188 g de CO2 par km',
      duration: 120,
      travelClass: 'Classe business',
      image: 'assets/LogoTexte_Traveleef_N.png',
      link: 'https://example.com/avion-madrid'
    },
    {
      destination: 'Madrid',
      price: 41,
      transport: 'Bus',
      carbonFootprint: '218 g de CO2 par km',
      duration: 480,
      travelClass: 'Classe économique',
      image: 'assets/LogoTexte_Traveleef_N.png',
      link: 'https://example.com/bus-madrid'
    },
    {
      destination: 'Madrid',
      price: 50,
      transport: 'Covoiturage',
      carbonFootprint: '100 g de CO2 par km',
      duration: 400,
      travelClass: 'Classe économique',
      image: 'assets/LogoTexte_Traveleef_N.png',
      link: 'https://example.com/covoiturage-madrid'
    },
    {
      destination: 'Madrid',
      price: 200,
      transport: 'Marin',
      carbonFootprint: '300 g de CO2 par km',
      duration: 600,
      travelClass: 'Classe business',
      image: 'assets/LogoTexte_Traveleef_N.png',
      link: 'https://example.com/marin-madrid'
    }
  ];

  // Filtres sélectionnés
  selectedClass: string = 'Toutes les classes';
  selectedTransport: string[] = [];
  priceRange = { min: 0, max: 200 };
  sortCriteria: string = 'eco';

  // Méthode pour appliquer les filtres
  getFilteredResults() {
    let filteredResults = this.results.filter((result) => {
      const classFilter = this.selectedClass === 'Toutes les classes' || result.travelClass === this.selectedClass;
      const transportFilter = this.selectedTransport.length === 0 || this.selectedTransport.includes(result.transport);

      // Gestion des valeurs min et max
      const minPrice = this.priceRange.min != null ? this.priceRange.min : 0;
      const maxPrice = this.priceRange.max != null ? this.priceRange.max : Number.MAX_VALUE;
      const priceFilter = result.price >= minPrice && result.price <= maxPrice;

      return classFilter && transportFilter && priceFilter;
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

  // Méthode pour trier
  sortBy(criteria: string) {
    this.sortCriteria = criteria;
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
