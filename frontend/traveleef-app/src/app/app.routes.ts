import { Routes } from '@angular/router';
import { InscriptionComponent } from './inscription/inscription.component';
import { ConnexionComponent } from './connexion/connexion.component';
import {PageResultatRechercheComponent} from "./page-resultat-recherche/page-resultat-recherche.component";



export const routes: Routes = [
    {path : 'inscription', component : InscriptionComponent},
    {path : 'connexion', component : ConnexionComponent},
    {path: 'results', component: PageResultatRechercheComponent},
    { path: '', redirectTo: '/connexion', pathMatch: 'full' }, // Redirection par défaut
];
