import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../service/authentification.service';
import { RouterLink } from '@angular/router';
import { FormsModule } from '@angular/forms';



@Component({
  selector: 'app-connexion',
  standalone: true,
  imports: [RouterLink,FormsModule],
  templateUrl: './connexion.component.html',
  styleUrls: ['./connexion.component.scss']
})

export class ConnexionComponent {
  credentials = { email: '', password: '' };

  constructor(private authService: AuthService, private router: Router) {}

  
  seConnecter(): void {
    //console.log('Données envoyées :', this.credentials);

    if (!this.credentials.email || !this.credentials.password) {
      console.error('Email et mot de passe sont requis');
      return;
    }

    this.authService.connexion(this.credentials).subscribe({
      next: (reponse) => {
        this.authService.stockerToken(reponse.token_acces);
        this.router.navigate(['/results']); // Redirection après connexion réussie
        console.log('Redirection effectuée vers /results');
      },
      error: (erreur) => {
        console.error('Erreur de connexion :', erreur);
      }
    });
  }
}
