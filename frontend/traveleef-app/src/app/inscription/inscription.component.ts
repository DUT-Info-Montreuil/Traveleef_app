import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { RouterLink, Router } from '@angular/router';
import { AuthService } from '../service/authentification.service';// Importer le service d'authentification

@Component({
  selector: 'app-inscription',
  templateUrl: './inscription.component.html',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, RouterLink],
  styleUrls: ['./inscription.component.css']
})
export class InscriptionComponent {
  registrationForm: FormGroup;
  message: string = ''; // Propriété pour stocker les messages

  constructor(private fb: FormBuilder, private authService: AuthService, private router: Router) {
  this.registrationForm = this.fb.group({
    first_name: ['', Validators.required],
    last_name: ['', Validators.required],
    email: ['', [Validators.required, Validators.email]],
    password: ['', [Validators.required, Validators.minLength(6)]],
    //confirmPassword: ['', Validators.required],
    role: ['user']  // Par défaut, l'utilisateur est un "user"
  },
  );
}

// Valider la correspondance des mots de passe
/*passwordMatchValidator(form: FormGroup) {
  return form.get('password')?.value === form.get('confirmPassword')?.value
    ? null
    : { passwordMismatch: true };
}*/

// Soumettre les données d'inscription
onSubmit() {
  console.log("test");

  if (this.registrationForm.valid) {
    console.log('if');
    const formValue = this.registrationForm.value;

    const utilisateur = {
      first_name: formValue.first_name,
      last_name: formValue.last_name,
      email: formValue.email,
      password: formValue.password,
      role: 'user'  // Prendre le rôle sélectionné ou 'user' par défaut
    };
    
    console.log(utilisateur);

    this.authService.inscription(utilisateur).subscribe({

      next: (response) => {
        console.log(response);
        this.message = 'Inscription réussie !';
        setTimeout(() => this.router.navigate(['/connexion']), 3000); // Rediriger après 3 secondes
      },
      error: (erreur) => {
        console.log(erreur);
        this.message = 'Une erreur est survenue lors de l\'inscription.';
        console.error('Erreur lors de l\'inscription :', erreur);
      }
    });
  } else {
    console.log('else');
    this.message = 'Veuillez remplir correctement le formulaire.';
  }
}
}
