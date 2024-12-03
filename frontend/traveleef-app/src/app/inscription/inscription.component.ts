import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { FooterComponent } from '../layout/footer/footer.component';
import { HeaderComponent } from '../layout/header/header.component';
import { RouterLink, Router } from '@angular/router';
import { AuthService } from '../service/authentification.service';// Importer le service d'authentification

@Component({
  selector: 'app-inscription',
  templateUrl: './inscription.component.html',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, FooterComponent, HeaderComponent, RouterLink],
  styleUrls: ['./inscription.component.css']
})
export class InscriptionComponent {
  registrationForm: FormGroup;
  message: string = ''; // Propriété pour stocker les messages

  constructor(private fb: FormBuilder, private authService: AuthService, private router: Router) {
    this.registrationForm = this.fb.group({
      name: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]],
      confirmPassword: ['', Validators.required]
    }, { validator: this.passwordMatchValidator });
  }

  // Valider la correspondance des mots de passe
  passwordMatchValidator(form: FormGroup) {
    return form.get('password')?.value === form.get('confirmPassword')?.value
      ? null
      : { passwordMismatch: true };
  }

  // Soumettre les données d'inscription
  onSubmit() {

    console.log("test");

    if (this.registrationForm.valid) {
      const formValue = this.registrationForm.value;

      const utilisateur = {
        email: formValue.email,
        mot_de_passe: formValue.password
      };

      this.authService.inscription(utilisateur).subscribe({
        next: (response) => {
          this.message = 'Inscription réussie !'; // Mettre à jour le message de succès
          setTimeout(() => this.router.navigate(['/connexion']), 3000); // Rediriger après 3 secondes
        },
        error: (erreur) => {
          this.message = 'Une erreur est survenue lors de l\'inscription.'; // Message d'erreur
          console.error('Erreur lors de l\'inscription :', erreur);
        }
      });
    } else {
      this.message = 'Veuillez remplir correctement le formulaire.';
    }
  }
}
