import { Routes } from '@angular/router';
import { InscriptionComponent } from './inscription/inscription.component';
import { ConnexionComponent } from './connexion/connexion.component';
import {PageResultatRechercheComponent} from "./page-resultat-recherche/page-resultat-recherche.component";
import { VoyageDetailComponent } from './voyage-detail/voyage-detail.component';



export const routes: Routes = [
    {path : 'inscription', component : InscriptionComponent},
    {path : 'connexion', component : ConnexionComponent},
    {path: 'results', component: PageResultatRechercheComponent},
    { path: 'voyage-detail', component: VoyageDetailComponent },
    { path: '', redirectTo: '/connexion', pathMatch: 'full' }, // Redirection par défaut
];
