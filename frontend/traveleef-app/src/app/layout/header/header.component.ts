import { Component } from '@angular/core';
import { AuthService } from '../../services/authentification.service';
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
    // S'abonner à l'état de connexion
    this.authService.isLoggedIn$.subscribe((loggedIn) => {
      this.isLoggedIn = loggedIn;
      if (loggedIn) {
        this.userName = 'Utilisateur'; // Chargez dynamiquement le nom si nécessaire
      }
    });
  }

  deconnexion(): void {
    this.authService.deconnexion();
    this.isLoggedIn = false;
  }

}
