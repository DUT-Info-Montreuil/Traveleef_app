import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../service/authentification.service';
import { FooterComponent } from '../layout/footer/footer.component';
import { HeaderComponent } from '../layout/header/header.component';
import { RouterLink } from '@angular/router';
import { FormsModule } from '@angular/forms';



@Component({
  selector: 'app-connexion',
  standalone: true,
  imports: [FooterComponent, HeaderComponent, RouterLink,FormsModule],
  templateUrl: './connexion.component.html',
  styleUrls: ['./connexion.component.scss']
})

export class ConnexionComponent {
  credentials = { email: '', mot_de_passe: '' };

  constructor(private authService: AuthService, private router: Router) {}

  seConnecter(): void {
    this.authService.connexion(this.credentials).subscribe({
      next: (reponse) => {
        this.authService.stockerToken(reponse.token_acces);
        this.router.navigate(['/dashboard']); // Redirection après connexion réussie
      },
      error: (erreur) => {
        console.error('Erreur de connexion :', erreur);
      }
    });
  }
}
