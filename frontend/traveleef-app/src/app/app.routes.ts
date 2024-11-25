import { Routes } from '@angular/router';
import { InscriptionComponent } from './inscription/inscription.component';
import { ConnexionComponent } from './connexion/connexion.component';




export const routes: Routes = [
    {path : 'inscription', component : InscriptionComponent},
    {path : 'connexion', component : ConnexionComponent}

];
