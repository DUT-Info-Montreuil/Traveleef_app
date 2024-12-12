import { Component } from '@angular/core';
import { AuthService } from '../../service/authentification.service';
import { RouterLink } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-header',
  standalone: true,
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss'],
  imports : [RouterLink,CommonModule]
})
export class HeaderComponent {
  isLoggedIn: boolean = false;
  userName: string = '';

  constructor(private authService: AuthService) {}

  ngOnInit(): void {
    // Vérifiez si l'utilisateur est connecté
    this.isLoggedIn = this.authService.estConnecte();
    if (this.isLoggedIn) {
      // Mettre à jour le nom de l'utilisateur si nécessaire
      this.userName = 'Utilisateur'; // Remplacez par une logique dynamique si disponible
    }
  }

  deconnexion(): void {
    this.authService.deconnexion();
    this.isLoggedIn = false;
  }

}