import { Component, OnInit } from '@angular/core';
import { VoyageService } from '../service/voyage.service';

@Component({
  selector: 'app-voyage-detail',
  templateUrl: './voyage-detail.component.html',
  styleUrls: ['./voyage-detail.component.scss'],
})
export class VoyageDetailComponent implements OnInit {
  voyageData: any;

  constructor(private voyageService: VoyageService) {}

  ngOnInit(): void {
    // Appel du service pour récupérer les données depuis le back-end
    this.voyageService.getVoyageDetails().subscribe((data) => {
      this.voyageData = data;
    });
  }
}
