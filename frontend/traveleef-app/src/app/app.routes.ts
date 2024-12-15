import { Routes } from '@angular/router';
import { InscriptionComponent } from './inscription/inscription.component';
import { ConnexionComponent } from './connexion/connexion.component';
import {PageResultatRechercheComponent} from "./page-resultat-recherche/page-resultat-recherche.component";
import {AccueilComponent} from "./features/accueil/page/accueil/accueil.component";


export const routes: Routes = [
    {path : 'inscription', component : InscriptionComponent},
    {path : 'connexion', component : ConnexionComponent},
    {path: 'results', component: PageResultatRechercheComponent},
    {path: "accueil", component: AccueilComponent},
    {path: "", redirectTo: "accueil", pathMatch: "full" },
];