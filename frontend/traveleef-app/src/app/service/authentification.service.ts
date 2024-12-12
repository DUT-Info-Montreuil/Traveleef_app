import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private apiUrl = 'http://localhost:5000/auth'; // Modifier selon l'URL de votre backend

  constructor(private http: HttpClient) {}

  /**
   * Inscription d'un utilisateur
   * @param utilisateur Contient email et mot_de_passe
   * @returns Observable avec la réponse du backend
   */
  inscription(utilisateur: { first_name: string; last_name: string; email: string; password : string; role: string }): Observable<any> {
    return this.http.post(`${this.apiUrl}/register`, utilisateur).pipe(
      catchError(this.handleError)
    );
  }

  /**
   * Connexion d'un utilisateur
   * @param credentials Contient email et mot_de_passe
   * @returns Observable avec token JWT et rôle utilisateur
   */
  connexion(credentials: { email: string; password: string }): Observable<any> {
    return this.http.post(`${this.apiUrl}/login`, credentials).pipe(
      catchError(this.handleError)
    );
  }

  /**
   * Stocker le token dans le localStorage
   * @param token JWT reçu après connexion
   */
  stockerToken(token: string): void {
    localStorage.setItem('token_acces', token);
  }

  /**
   * Récupérer le token du localStorage
   * @returns Token JWT ou null
   */
  recupererToken(): string | null {
    return localStorage.getItem('token_acces');
  }

  /**
   * Vérifie si l'utilisateur est connecté
   * @returns boolean
   */
  estConnecte(): boolean {
    return !!this.recupererToken();
  }

  /**
   * Déconnexion : suppression du token
   */
  deconnexion(): void {
    localStorage.removeItem('token_acces');
  }

  /**
   * Gestion des erreurs HTTP
   * @param erreur Erreur HTTP capturée
   * @returns Observable contenant l'erreur formatée
   */
  private handleError(erreur: HttpErrorResponse): Observable<never> {
    let messageErreur = 'Une erreur inconnue s\'est produite';
    if (erreur.error instanceof ErrorEvent) {
      // Erreur côté client
      messageErreur = `Erreur : ${erreur.error.message}`;
    } else {
      // Erreur côté serveur
      messageErreur = `Erreur ${erreur.status} : ${erreur.message}`;
    }
    return throwError(messageErreur);
  }
}
