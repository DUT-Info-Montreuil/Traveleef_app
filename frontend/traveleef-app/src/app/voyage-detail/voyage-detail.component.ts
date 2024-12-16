import { Component, OnInit } from '@angular/core';
import {Router, RouterLink} from '@angular/router';
import {CurrencyPipe, DatePipe, NgForOf, NgIf} from "@angular/common";
import {SearchBarComponent} from "../shared/components/search-bar/search-bar.component";

@Component({
  selector: 'app-voyage-detail',
  templateUrl: './voyage-detail.component.html',
  styleUrls: ['./voyage-detail.component.scss'],
  imports: [
    DatePipe,
    NgForOf,
    CurrencyPipe,
    NgIf,
    RouterLink,
    SearchBarComponent
  ],
  standalone: true
})
export class VoyageDetailComponent implements OnInit {
  flight: any;
  emissions: any = {};
  allerFlights: any[] = [];
  retourFlights: any[] = [];

  constructor(private router: Router) {}

  ngOnInit() {
    this.flight = history.state.flight;

    if (this.flight && this.flight.carbon_emissions) {
      this.emissions = this.flight.carbon_emissions;
    } else {
      this.emissions = {
        difference_percent: 0,
        this_flight: 0,
        typical_for_this_route: 0
      };
    }

    this.allerFlights = this.flight.flights.filter((flight: { direction: string; }) => flight.direction === 'aller');
    this.retourFlights = this.flight.flights.filter((flight: { direction: string; }) => flight.direction === 'retour');
  }
}
