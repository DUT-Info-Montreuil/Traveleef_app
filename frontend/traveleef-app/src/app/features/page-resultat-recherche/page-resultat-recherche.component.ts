import {Component, OnInit} from '@angular/core';
import { CommonModule, NgOptimizedImage } from '@angular/common';
import { FormsModule } from '@angular/forms';
import {TravelService} from "../../services/travel.service";
import {ActivatedRoute, RouterLink} from "@angular/router";
import {SearchBarComponent} from "../../shared/components/search-bar/search-bar.component";

@Component({
  selector: 'app-page-resultat-recherche',
  standalone: true,
  imports: [CommonModule, FormsModule, NgOptimizedImage, RouterLink, SearchBarComponent],
  templateUrl: './page-resultat-recherche.component.html',
  styleUrls: ['./page-resultat-recherche.component.scss']
})
export class PageResultatRechercheComponent implements OnInit {

  searchData: any;
  bestFlights: any[] = [];

  constructor(private router: ActivatedRoute, private travelService: TravelService) { }

  ngOnInit(): void {
    this.router.paramMap.subscribe(() => {
      this.searchData = history.state['data'];
      if (this.searchData) {
        this.travelService.searchFlights(this.searchData).subscribe(
          response => {
            if (response && response.best_flights) {
              this.bestFlights = response.best_flights.map((flight: any) => ({
                airline_logo: flight.airline_logo,
                airline: flight.airline,
                price: flight.price,
                total_duration: flight.total_duration,
                flights: flight.flights,
                extensions: flight.extensions,
                carbon_emissions: flight.carbon_emissions,
                transport: 'Avion',
              }));
            }
          },
          error => {
            console.error('Erreur lors de la récupération des vols :', error);
          }
        );
      } else {
        console.log('Aucune donnée reçue');
      }
    });
  }

  // Filtres sélectionnés
  selectedClass: string = 'Toutes les classes';
  selectedTransport: string[] = [];
  priceRange = { min: 0, max: 5000 };
  sortCriteria: string = 'eco';

  getFilteredResults(): any[] {

    if (!this.bestFlights || this.bestFlights.length === 0) {
      return [];
    }

    const filteredFlights = this.bestFlights.filter((flight) => {
      const minPrice = this.priceRange?.min || 0;
      const maxPrice = this.priceRange?.max || Number.MAX_VALUE;
      const matchesPrice = flight.price >= minPrice && flight.price <= maxPrice;

      const matchesClass =
        this.selectedClass === 'Toutes les classes' ||
        flight.flights[0]?.travel_class === this.selectedClass;

      const matchesTransport =
        this.selectedTransport.length === 0 ||
        this.selectedTransport.includes(flight.flights[0]?.transport);

      console.log("Flight:", flight, {
        matchesPrice,
        matchesClass,
        matchesTransport
      });

      return matchesPrice && matchesClass && matchesTransport;
    });

    const sortedFlights = filteredFlights.sort((a, b) => {
      if (this.sortCriteria === 'price') {
        return a.price - b.price;
      } else if (this.sortCriteria === 'duration') {
        return a.total_duration - b.total_duration;
      } else if (this.sortCriteria === 'eco') {
        return parseFloat(a.carbon_emissions?.this_flight || '0') -
          parseFloat(b.carbon_emissions?.this_flight || '0');
      }
      return 0;
    });

    return sortedFlights;
  }


  // Méthode pour trier
  sortBy(criteria: string) {
    this.sortCriteria = criteria;
  }

  // Méthode pour ajuster les filtres
  setPriceRange(min: number , max: number) {
    this.priceRange = { min, max };
  }

  setClassFilter(selectedClass: string) {
    this.selectedClass = selectedClass;
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
