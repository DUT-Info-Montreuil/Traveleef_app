import {Component, OnInit} from '@angular/core';
import {SearchBarComponent} from "../../../../shared/components/search-bar/search-bar.component";
import {MapComponent} from "../../../../shared/components/map/map.component";
import {NgForOf, NgIf} from "@angular/common";
import {RouterLink} from "@angular/router";
import {ImageService} from "../../../../services/image.service";

@Component({
  selector: 'app-accueil',
  standalone: true,
  imports: [
    SearchBarComponent,
    MapComponent,
    NgForOf,
    RouterLink,
    NgIf
  ],
  templateUrl: './accueil.component.html',
  styleUrl: './accueil.component.scss'
})
export class AccueilComponent implements OnInit{

  constructor(private imageService: ImageService) {
  }

  cards = [
    {
      title: 'Madrid',
      description: 'Découvrez Madrid, une ville magnifique à visiter.',
      price: 41,
      carbonFootprint: 176,
      image: '',
    },
    {
      title: 'Barcelone',
      description: 'Explorez la beauté de Barcelone.',
      price: 55,
      carbonFootprint: 200,
      image: '',
    }
  ];

  error: string = '';


  ngOnInit() {
    this.cards.forEach(card => {
      const city = card.title;
      this.fetchImage(card);
    });
  }

  fetchImage(card: any) {
    this.imageService.getImage(`${card.title} cityscape`).subscribe(
      (data) => {
        if (data.results && data.results.length > 0) {
          card.image = data.results[0].urls.regular;
          this.error = '';
        } else {
          this.error = 'Aucune image trouvée pour cette recherche.';
        }
      },
      (err) => {
        this.error = 'Erreur lors de la récupération de l\'image.';
        console.error(err);
      }
    );
  }

}
