import { Routes } from '@angular/router';
import { InscriptionComponent } from './features/inscription/inscription.component';
import { ConnexionComponent } from './features/connexion/connexion.component';
import {PageResultatRechercheComponent} from "./features/page-resultat-recherche/page-resultat-recherche.component";
import {AccueilComponent} from "./features/accueil/page/accueil/accueil.component";
import { VoyageDetailComponent } from './features/voyage-detail/voyage-detail.component';


export const routes: Routes = [
    {path : 'inscription', component : InscriptionComponent},
    {path : 'connexion', component : ConnexionComponent},
    {path: 'results', component: PageResultatRechercheComponent},
    {path: "accueil", component: AccueilComponent},
    {path: "", redirectTo: "accueil", pathMatch: "full" },
    { path: 'voyage-detail', component: VoyageDetailComponent },
]
